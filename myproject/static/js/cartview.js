window.onload = function(){
    storage = window.sessionStorage;
    var cartList = storage.cart;
    product_table = document.getElementById("item-list");
    fetch("/cart/",{
        credentials: "same-origin",
        mode: "same-origin",
        method: "post",
        headers: { "Content-Type": "application/json" },
        body: cartList
    }).then(data=>{
        return data.json();
    }).then(data=>{
        products = data.data;
        for(var i=0;i<products.length;i++){
            var tr = product_table.insertRow(-1);
            tr.innerHTML = `
            <td>
                <div class="img">
                    <a href="#"><img src="${products[i].image}" alt="Image"></a>
                    <p>${products[i].name}</p>
                </div>
            </td>
            <td><button class="btn-cart">200KG</button></td>
            <td>$99</td>
            <td>
                <div class="qty">
                    <button class="btn-minus"><i class="fa fa-minus"></i></button>
                    <input type="text" value="1">
                    <button class="btn-plus"><i class="fa fa-plus"></i></button>
                </div>
            </td>
            <td>$99</td>
            <td><button><i class="fa fa-trash"></i></button></td>
            `;
        }
    })
}

{/* <tr>
<td>
    <div class="img">
        <a href="#"><img src="{{product.image}}" alt="Image"></a>
        <p>{{product.name}}</p>
    </div>
</td>
<td><button class="btn-cart">200KG</button></td>
<td>$99</td>
<td>
    <div class="qty">
        <button class="btn-minus"><i class="fa fa-minus"></i></button>
        <input type="text" value="1">
        <button class="btn-plus"><i class="fa fa-plus"></i></button>
    </div>
</td>
<td>$99</td>
<td><button><i class="fa fa-trash"></i></button></td>
</tr> */}