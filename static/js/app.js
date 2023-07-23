document.addEventListener('prechange', function(event) {
  document.querySelector('ons-toolbar .center')
    .innerHTML = event.tabItem.getAttribute('label');
});

var sendCommand = function(chassis, mode, op) {
    let url = "?chassis=" + chassis + "&mode=" + mode + "&op=" + op
    fetch(url)
}

var inputSwitch = function() {
    fetch('?mode=route&op=1')
}

var lcdTest = function() {
    fetch('?mode=lcdtest')
}

var showCmdDialog = function() {
  var dialog = document.getElementById('command-sent');

  if (dialog) {
    dialog.show();
  } else {
    ons.createElement('dialog.html', { append: true })
      .then(function(dialog) {
        dialog.show();
      });
  }
};

var hideDialog = function(id) {
  document
    .getElementById(id)
    .hide();
};