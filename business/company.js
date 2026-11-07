/* Local only. Copies the brief already on the page. No network request. */
(function () {
  var button = document.getElementById("copy-brief");
  var brief = document.getElementById("brief");
  var status = document.getElementById("copy-status");
  if (!button || !brief) return;

  function say(message) {
    if (status) status.textContent = message;
  }

  button.addEventListener("click", function () {
    var text = brief.innerText.replace(/\n{3,}/g, "\n\n").trim();
    if (!navigator.clipboard || !navigator.clipboard.writeText) {
      button.textContent = "Select the brief and copy";
      say("Clipboard is unavailable. Select the brief and copy it.");
      return;
    }
    navigator.clipboard.writeText(text).then(function () {
      button.textContent = "Copied";
      say("Evaluation brief copied.");
    }).catch(function () {
      button.textContent = "Select the brief and copy";
      say("Clipboard is unavailable. Select the brief and copy it.");
    });
  });
})();
