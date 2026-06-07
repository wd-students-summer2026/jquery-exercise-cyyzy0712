$(function () {
    var uxTerms = [
      "Affordance \u2014 a visual cue that signals how an element should be used.",
      "Information architecture \u2014 how content is organized so users can find it.",
      "Heuristic evaluation \u2014 reviewing an interface against usability principles.",
      "Progressive disclosure \u2014 revealing complexity only when the user needs it.",
      "Cognitive load \u2014 the mental effort required to use an interface."
    ];
    var termIndex = 0;
    $("#reveal-btn").on("click", function () {
      $("#definition").text(uxTerms[termIndex]);
      termIndex = (termIndex + 1) % uxTerms.length; // cycle through terms
    });
  
    $("#swap-image").on("mouseover", function () {
      $(this).attr("src", $(this).data("swap"));
    });
    $("#swap-image").on("mouseout", function () {
      $(this).attr("src", $(this).data("original"));
    });
  
    var moverOut = false;
    $("#move-btn").on("click", function () {
      if (!moverOut) {
        $("#mover").animate({ left: "250px", top: "20px" }, 600);
        $("#mover").text("shipped \uD83D\uDE80");
      } else {
        $("#mover").animate({ left: "0px", top: "0px" }, 600);
        $("#mover").text("concept");
      }
      moverOut = !moverOut;
    });
  
    $("#shake-btn").on("click", function () {
      $("#shake-target")
        .velocity({ translateX: "-12px" }, { duration: 80 })
        .velocity({ translateX: "12px" }, { duration: 80 })
        .velocity({ translateX: "-8px" }, { duration: 80 })
        .velocity({ translateX: "8px" }, { duration: 80 })
        .velocity({ translateX: "0px" }, { duration: 80 });
    });
  })