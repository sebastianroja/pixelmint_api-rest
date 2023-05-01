
$(document).ready(function() {
    setInterval(function() {
      $.get("http://worldtimeapi.org/api/timezone/europe/london", function(data) {
        var londonTime = data.datetime.slice(11, 16); // Obtiene solo la hora y minutos
        var formattedTime = moment(londonTime, "HH:mm").format("h:mm A"); // Da formato a la hora
        $("#hora-londres").text("Londres: " + formattedTime);
      });
    }, 1000); // Actualiza la hora cada 1 segundo
  });

  
$(document).ready(function() {
    setInterval(function() {
      $.get("http://worldtimeapi.org/api/timezone/America/Santiago", function(data) {
        var londonTime = data.datetime.slice(11, 16); // Obtiene solo la hora y minutos
        var formattedTime = moment(londonTime, "HH:mm").format("h:mm A"); // Da formato a la hora
        $("#hora-chile").text("Chile: " + formattedTime);
      });
    }, 1000); // Actualiza la hora cada 1 segundo
  });
  
$(document).ready(function() {
setInterval(function() {
    $.get("http://worldtimeapi.org/api/timezone/Asia/Dubai", function(data) {
    var londonTime = data.datetime.slice(11, 16); // Obtiene solo la hora y minutos
    var formattedTime = moment(londonTime, "HH:mm").format("h:mm A"); // Da formato a la hora
    $("#hora-dubai").text("Dubai: " + formattedTime);
    });
}, 1000); // Actualiza la hora cada 1 segundo
});
function obtenerRateUSDCLP() {
    fetch("https://www.freeforexapi.com/api/live?pairs=USDCLP")
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        var rate = data.rates.USDCLP.rate;
        var divRate = document.getElementById("rate");
        divRate.innerHTML = "El rate USD/CLP es " + rate;
      });
  }
  
  obtenerRateUSDCLP();
  