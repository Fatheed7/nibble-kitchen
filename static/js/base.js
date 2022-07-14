$(document).ready(function () {
  $(".header-container").css("padding-top", $("header").height() + 31.03);
  $(".toast").toggleClass("toast-animation");

  setTimeout(
    function () {
      $(".toast").removeClass("toast-animation");
    },

    5000
  );

  if (document.body.scrollHeight < $(window).height()) {
    $("footer").addClass("position-absolute bottom-0 start-0");
  } else {
    $("footer").addClass("position-static");
  }
});

$(".btn-close").click(function () {
  $(".toast").toggleClass("toast-animation");
});

window.addEventListener("load", function () {
  baguetteBox.run(".gallery", {
    captions: function (element) {
      return element.getElementsByTagName("img")[0].alt;
    },
  });
});

$(".search-button").click(function () {
  if ($(".search-box").val().length === 0) {
    event.preventDefault();
    $(".invalid-tooltip").show();

    setTimeout(
      function () {
        $(".invalid-tooltip").fadeOut("fast");
      },

      5000
    );
  }
});

$(".mobile-search-button").click(function () {
  if ($(".mobile-search-box").val().length === 0) {
    event.preventDefault();
    $(".invalid-tooltip").show();

    setTimeout(
      function () {
        $(".invalid-tooltip").fadeOut("fast");
      },

      5000
    );
  }
});

$(window).resize(function () {
  if ($(this).width() > 992) {
    $("#user-options-div").addClass("d-none");
    $("#mobile-search-div").addClass("d-none");
  } else {
    $("#user-options-div").removeClass("d-none");
    $("#mobile-search-div").removeClass("d-none");
  }

  $(".header-container").css("padding-top", $("header").height());
});
