$("#roll-btn").click(function () {
  $.post("/roll", {}, function (data) {
    $("#turn-number").text(data.turn);
    $("#roll-results").html(
      `<strong>Wynik rzutu:</strong> ${data.dice.join(", ")}`
    );

    for (const [animal, count] of Object.entries(data.animals)) {
      $(`#${animal}-count`).text(count);
    }

    if (data.event.length > 0) {
      $("#event-log").removeClass("d-none").html(data.event.join("<br>"));
    } else {
      $("#event-log").addClass("d-none");
    }

    renderTrades(data.trades);
    $("#alert-box").addClass("d-none").text("");
    $("#trades-left").text("1");

    if (data.victory) {
      $("#victory-msg").removeClass("d-none");
    }
  });
});

function renderTrades(trades) {
  const container = $("#trade-options");
  container.empty();

  if (trades.length === 0) {
    container.html("<p>Brak możliwych wymian w tej turze.</p>");
    return;
  }

  const animalNames = {
    rabbit: "królików",
    sheep: "owiec",
    pig: "świń",
    cow: "krów",
    horse: "koni",
    small_dog: "małych psów",
    big_dog: "dużych psów",
  };

  for (const trade of trades) {
    const cost = trade.cost;
    const from = trade.from;
    const to = trade.to;
    const receive = trade.receive ?? 1;

    const btn = $(`
          <div class="col-6 col-md-4 mb-2">
            <button class="btn btn-outline-success w-100">
              ${cost} ${animalNames[from] || from} ➡️ ${receive} ${
      animalNames[to] || to
    }
            </button>
          </div>
        `);

    btn.click(() => {
      $.ajax({
        url: "/trade",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({ from, to }),
        success: function (data) {
          for (const [animal, count] of Object.entries(data.animals)) {
            $(`#${animal}-count`).text(count);
          }
          renderTrades(data.trades);
          $("#trades-left").text(data.can_trade ? "1" : "0");
          if (!data.success) {
            showAlert(data.message);
          }
        },
      });
    });

    container.append(btn);
  }
}
