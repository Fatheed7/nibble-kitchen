import "../css/styles.css" assert { type: "css" };
import {
  debounce,
  autocompleteAddress,
  getDetailsAddress,
} from "./autocomplete.js";
let componentsRestriction = [];
const woosmap_key = "woos-1bd4a9d1-f795-3334-930f-d5ec68a29651";

function displayAddress() {
  const value = document.getElementById("input").value;
  const results = document.querySelector(".autocomplete-results");

  let components = componentsRestriction.map(({ id }) => `country:${id}`);
  components = components.join("|");
  let language = "";

  autocompleteAddress(value, components, language, woosmap_key).then(
    ({ predictions }) => {
      results.innerHTML = "";
      results.parentElement.style.display = "none";
      let html = "";
      for (let prediction_id in predictions || []) {
        let prediction = predictions[prediction_id];
        let predictionClass = "no-viewpoint";

        let matched_substrings = prediction.matched_substring.description;
        let formatted_name = bold_matched_substring(
          prediction["description"],
          matched_substrings
        );

        if (prediction.postal_codes) {
          formatted_name += ` (${prediction.postal_codes.join(", ")})`;
        }
        if (prediction.viewpoint) {
          predictionClass = "has-viewpoint";
        }

        html += `<div class="prediction ${predictionClass}" prediction-id=${prediction_id}>${formatted_name}</div>`;
      }

      results.innerHTML = html;
      results.style.display = "block";
      results.parentElement.style.display = "flex";

      const data = results.querySelectorAll(".prediction");

      for (let result of data) {
        result.addEventListener("click", () => {
          results.style.display = "none";
          results.parentElement.style.display = "none";
          const predictionId = parseInt(
            result.getAttribute("prediction-id"),
            10
          );
          const prediction = predictions[predictionId];
          document.getElementById("input").value = prediction.description;
          const fields = [
            ...document.querySelectorAll('input[name="fields"]:checked'),
          ].map((e) => e.value);
          getDetailsAddress(
            prediction.public_id,
            components,
            fields.join("|"),
            woosmap_key
          ).then((addressDetails) => {
            if (addressDetails.status !== "OK") {
              return;
            }
            displayAddressDetails(addressDetails.result);
          });
        });
      }
    }
  );
}

function bold_matched_substring(string, matched_substrings) {
  matched_substrings = matched_substrings.reverse();
  for (let substring of matched_substrings) {
    let char = string.substring(
      substring["offset"],
      substring["offset"] + substring["length"]
    );
    string = `${string.substring(
      0,
      substring["offset"]
    )}<span class='bold'>${char}</span>${string.substring(
      substring["offset"] + substring["length"]
    )}`;
  }
  return string;
}

function displayAddressDetails(addressDetails) {
  if (addressDetails.formatted_address) {
    $("#id_street_address1").val(
      addressDetails.address_components[7].long_name +
        " " +
        addressDetails.address_components[5].long_name
    );
    $("#id_street_address2").val(
      addressDetails.address_components[4].long_name
    );
    $("#id_town_or_city").val(addressDetails.address_components[3].long_name);
    $("#id_postcode").val(addressDetails.address_components[6].long_name);
    $("#id_county").val(addressDetails.address_components[2].long_name);
  }
}

function initUI() {
  const overlayCb = document.getElementById("bgOverlay");
  const results = document.querySelector(".autocomplete-results");
  const input = document.querySelector(".autocomplete-input > input");
  let componentExpanded = false;
  input.addEventListener(
    "input",
    debounce(function () {
      let value = this.value;
      value.replace('"', '\\"').replace(/^\s+|\s+$/g, "");
      if (value !== "") {
        displayAddress(value);
      } else {
        results.innerHTML = "";
      }
    }, 0)
  );
}

initUI();
