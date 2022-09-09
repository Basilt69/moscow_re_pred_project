
function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var area_total = document.getElementById("uiSqmt");
  var kitchen_area = document.getElementById("uiKitchSqmt");
  var floors_total = document.getElementById("uiFloors");
  var floor_number = document.getElementById("uiFloorDes");
  var location = document.getElementById("uiLocations");
  var material = document.getElementById("uiMaterials");
  var estPrice = document.getElementById("uiEstimatedPrice");

  //var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx
  var url = "/api/predict_home_price/"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  var data = {
    area_total:parseFloat(area_total.value),
    kitchen_area:parseFloat(kitchen_area.value),
    floors_total:parseInt(floors_total.value),
    floor_number:parseInt(floor_number.value),
    location:location.value,
    material:material.value
  }

  console.log(data)

  $.post(url, {
      area_total: parseFloat(area_total.value),
      kitchen_area: parseFloat(kitchen_area.value),
      floors_total: parseInt(floors_total.value),
      floor_number: parseInt(floor_number.value),
      location: location.value,
      material: material.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Rub</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  //var url_1 = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx
  var url_1 = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url_1,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
  //var url_2 = "http://127.0.0.1:5000/get_material_names"; // Use this if you are NOT using nginx
  var url_2 = "/api/get_material_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url_2,function(data, status) {
      console.log("got response for get_material_names request");
      if(data) {
          var materials = data.materials;
          var uiMaterials = document.getElementById("uiMaterials");
          $('#uiMaterials').empty();
          for(var i in materials) {
              var opt = new Option(materials[i]);
              $('#uiMaterials').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;