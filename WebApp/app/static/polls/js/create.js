
function find_prod_index() {
    // Finding the next index of product (if page was refreshed)
    let index=1;
    for (let j=0; j<30; j++) {
        var check=document.getElementById('repeate_'+j);
        if (check) {
           index=j+1;
        }
    }
    return index;
}
function find_step_index() {
    let index=1;
    for (let j=0; j<30; j++) {
        var check=document.getElementById('step_repeate_'+j);
        if (check) {
           index=j+1;
        }
    }
    return index;
}

$(document).ready(function() {
    /* Recipe Creation */
    // "Add ingredient" button click handling
    let i=find_prod_index();
    $("#add").click(function() {
        // Adding new fields for next ingredient (ingredient name and weight)
        $("#ingredientAdd").append('<div class="form-group">' +
'        <label for="name_'+i+'">'+(i+1)+' Product name</label>' +
'        <input list="products" name="name_'+i+'" class="form-control" placeholder="Product name"></input>' +
'        <datalist id="products">' +
'            {% for product in products %}' +
'                <option class="upper-first" value="{{ product.name }}"></option>' +
'            {% endfor %}' +
'            {% for product in r_products %}' +
'                <option class="upper-first" value="{{ product.name }}"></option>' +
'            {% endfor %}' +
'        </datalist>' +    
'        <div id="weight"><div class="form-group">' + 
'            <label for="weight_'+i+'">Amount</label>' + 
'            <input type="number" step="0.01" name="weight_'+i+'" placeholder="0.00"' + 
'               class="form-control" value=""></input></div>' + 
'       <div class="form-group">' + 
'           <label for="weight-type_'+i+'">Weight type</label>' + 
'           <input type="text" name="weight-type_'+i+'" placeholder="kg, g, l, ml, pcs, etc."' + 
'               class="form-control" value=""></input>' + 
'       </div></div>');
        // Changing index
        i++;
        // Hide adding button if 30 ingredients was added
        if (i >= 30) {
            $(this).hide();
        }
    });

    let step=find_step_index();
    $("#addStep").click(function() {
        // Adding new fields for next step
        $("#stepAdd").append('<div class="form-group">' +
'        <label for="step_'+step+'">Step '+(step+1)+'</label>' +
'        <textarea name="step_'+step+'" class="form-control" placeholder="What should be done in step '+(step+1)+'?"></textarea>' +
'        </div>');
        // Changing index
        step++;
        // Hide adding button if 30 ingredients was added
        if (step >= 30) {
            $(this).hide();
        }
    });
});