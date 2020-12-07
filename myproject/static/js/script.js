function cartCount(){
    cart = document.getElementById("cart-item-count");
    fetch(`/getCartCount`).then(response=>{
        return response.json();
    }).then(data=>{
        count = data.itemCount;
        cart.innerText = `(${count})`;
    });
};

function addToCart(productId){
    fetch(`/addToCart/${productId}`).then(response=>{
        return response.json();
    }).then(()=>{
        cartCount();
    });
}

function wishCount(){
    cart = document.getElementById("wish-item-count");
    fetch(`/getWishtCount`).then(response=>{
        return response.json();
    }).then(data=>{
        count = data.itemCount;
        cart.innerText = `(${count})`;
    });
};

function addToWish(productId){
    fetch(`/addToWish/${productId}`).then(response=>{
        return response.json();
    }).then(()=>{
        wishCount();
    });
}

window.onload = function(){
    cartCount();
    wishCount();
};

