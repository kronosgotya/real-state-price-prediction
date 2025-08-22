const API_BASE = "http://127.0.0.1:5000";

function getRadioValue(name) {
  const nodes = document.getElementsByName(name);
  for (let i = 0; i < nodes.length; i++) if (nodes[i].checked) return parseInt(nodes[i].value, 10);
  return -1;
}

function onClickedEstimatePrice() {
  const sqftVal = parseFloat(document.getElementById("uiSqft").value);
  const broom = getRadioValue("uiBroom");
  const bath = getRadioValue("uiBathrooms");
  const location = document.getElementById("uiLocations").value;
  const url = `${API_BASE}/predict_home_price`;

  $.post(url, { sqft: sqftVal, broom: broom, bath: bath, location: location })
    .done(data => {
      document.getElementById("uiEstimatedPrice").innerHTML =
        data && data.estimated_price != null
          ? `<h2>${data.estimated_price} Lakh</h2>`
          : `<h2>Error</h2>`;
    })
    .fail((jq, t, e) => console.error("POST failed:", t, e, jq.status, jq.responseText));
}

function onPageLoad() {
  const url = `${API_BASE}/get_location_names`;
  $.get(url)
    .done(data => {
      const $sel = $("#uiLocations").empty();
      $sel.append(new Option("Choose a Location", "", true, false));
      if (data && Array.isArray(data.locations)) {
        data.locations.forEach(loc => $sel.append(new Option(loc, loc)));
      } else {
        console.warn("Respuesta sin locations:", data);
      }
    })
    .fail((jq, t, e) => console.error("GET failed:", t, e, jq.status, jq.responseText));
}

window.onload = onPageLoad;