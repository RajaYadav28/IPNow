function copyIP() {
  var ipText = document.getElementById('ipAddress').innerText;
  var tempInput = document.createElement('input');
  tempInput.value = ipText;
  document.body.appendChild(tempInput);
  tempInput.select();
  document.execCommand('copy');
  document.body.removeChild(tempInput);

  var successMessage = document.getElementById('successMessage');
  successMessage.style.display = 'block';

  setTimeout(function () {
    successMessage.style.display = 'none';
  }, 3000);
}
