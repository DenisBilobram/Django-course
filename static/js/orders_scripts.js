function update_total_cost() {
    let forms_count = document.getElementById("id_orderitems-TOTAL_FORMS").getAttribute("value");
    let sum = 0;
    for (let i = 0; i < forms_count; i++) {
        try {
            price = document.getElementById(`id_orderitems-${i}-price`).value;;
            price = parseInt(price);
            if (isNaN(price)) continue;
        } catch (e) {
            continue;
        }
        sum += price;
    }
    let cost = document.querySelector('.order_total_cost');
    cost.innerHTML = sum;
}
function update_total_count() {
    let forms_count = document.getElementById("id_orderitems-TOTAL_FORMS").getAttribute("value");
    let sum = 0;
    for (let i = 0; i < forms_count; i++) {
        try {
            count = document.getElementById(`id_orderitems-${i}-quantity`).value;
            count = parseInt(count);
            if (isNaN(count)) continue;
        } catch (e) {
            continue;
        }
        sum += count;
    }
    let quantity = document.querySelector('.order_total_quantity');
    quantity.innerHTML = sum
}

function delete_row(row) {
    try {
        row[0].remove();
        let price = parseInt(row[0].querySelector('input[type="text"]').value);
        let cost = parseInt(document.querySelector('.order_total_cost').innerText);
        if (!isNaN(price)) cost -= price;
        document.querySelector('.order_total_cost').innerHTML = cost;
        let el = document.querySelector('.order_total_quantity');
        count = row[0].querySelector('input[type="number"]').value;
        result = parseInt(el.innerText) - count;
        el.innerHTML = result;
    } catch (e) {
        console.log('empty')
    }
}

function update_cost(event) {
    let i = event.target.id.replace('id_orderitems-', '').replace('-quantity', '');
    let price_for_one = event.target.getAttribute('price_for_one');
    document.getElementById(`id_orderitems-${i}-price`).value = price_for_one * event.target.value
    update_total_cost();
    update_total_count();
}

function update_prod(event) {
    let i = event.target.id.replace('id_orderitems-', '').replace('-product', '');
    let value = event.target.value
    let product = document.querySelector(`option[value="${value}"]`).innerText
    let quantity = document.querySelector(`#id_orderitems-${i}-quantity`)
    $.ajax({
        url: '../../orders/products_get',
        type: 'get',
        data: {
            product_name: product
        },
        success: function(response) {
            quantity.setAttribute('price_for_one', response.price);
            quantity.dispatchEvent(new Event("change"));
        }
    })
}
function new_row(row) {
    let product = row[0].querySelector("select")
    let quantity = row[0].querySelector('input[type="number"]')
    quantity.value = 0
    product.addEventListener("change", update_prod)
    quantity.addEventListener("change", update_cost)
}

window.onload = function () {
    let forms_count = document.getElementById("id_orderitems-TOTAL_FORMS").getAttribute("value")

    for (let i = 0; i < forms_count; i++) {
        let el = document.getElementById(`id_orderitems-${i}-quantity`);
        try {
            price = document.getElementById(`id_orderitems-${i}-price`).value;
        } catch (e) {
            el = document.getElementById(`id_orderitems-${i}-product`);
            el.addEventListener('change', update_prod);
            el = document.querySelector(`#id_orderitems-${i}-quantity`)
            el.addEventListener('change', update_cost);
            continue
        }
        let quantity = el.defaultValue;
        el.setAttribute('price_for_one', `${ price / quantity }`);
        el.addEventListener('change', update_cost);
        let prod = document.getElementById(`id_orderitems-${i}-product`);
        prod.addEventListener('change', update_prod);
    }
    $('.formset_row').formset({
        addText: 'добавить продукт',
        deleteText: 'удалить',
        prefix: 'orderitems',
        removed: delete_row,
        added: new_row,
     });
}