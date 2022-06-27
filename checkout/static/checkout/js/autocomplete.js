export function autocompleteAddress(input, components, language, woosmap_key) {
  const args = {
    key: woosmap_key,
    input,
    components: "country:gb",
  };

  if (components !== "") {
    args.components = components;
  }

  if (language !== "") {
    args.language = language;
  }

  return fetch(
    `https://api.woosmap.com/address/autocomplete/json?${buildQueryString(
      args
    )}`
  ).then((response) => response.json());
}

export function getDetailsAddress(publicId, components, fields, woosmap_key) {
  const args = {
    key: woosmap_key,
    public_id: publicId,
    components: "country:gb",
  };

  if (components !== "") {
    args.components = components;
  }

  if (fields) {
    args.fields = fields;
  }

  return fetch(
    `https://api.woosmap.com/address/details/json?${buildQueryString(args)}`
  ).then((response) => response.json());
}

export function buildQueryString(params) {
  const queryStringParts = [];

  for (let key in params) {
    if (params.hasOwnProperty(key)) {
      let value = params[key];
      queryStringParts.push(
        `${encodeURIComponent(key)}=${encodeURIComponent(value)}`
      );
    }
  }

  return queryStringParts.join("&");
}

export function debounce(func, wait, immediate) {
  let timeout;
  return function () {
    const context = this;
    const args = arguments;
    const later = () => {
      timeout = null;
      if (!immediate) {
        func.apply(context, args);
      }
    };
    const callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) {
      func.apply(context, args);
    }
  };
}
