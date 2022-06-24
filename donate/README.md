# Donate
## PayPal!
## ---------------------------------Paypal----------------------------------
<div id="smart-button-container">
    <div style="text-align: center"><label for="description">Donate Here! </label><input type="text" name="descriptionInput" id="description" maxlength="127" value=""></div>
      <p id="descriptionError" style="visibility: hidden; color:red; text-align: center;">Please enter a description</p>
    <div style="text-align: center"><label for="amount">Number to donate </label><input name="amountInput" type="number" id="amount" value="" ><span> USD</span></div>
      <p id="priceLabelError" style="visibility: hidden; color:red; text-align: center;">Please enter a price</p>
    <div id="invoiceidDiv" style="text-align: center; display: none;"><label for="invoiceid"> </label><input name="invoiceid" maxlength="127" type="text" id="invoiceid" value="" ></div>
      <p id="invoiceidError" style="visibility: hidden; color:red; text-align: center;">Please enter an Invoice ID</p>
    <div style="text-align: center; margin-top: 0.625rem;" id="paypal-button-container"></div>
  </div>
  <script src="https://www.paypal.com/sdk/js?client-id=sb&enable-funding=venmo&currency=USD" data-sdk-integration-source="button-factory"></script>
  <script>
  function initPayPalButton() {
    var description = document.querySelector('#smart-button-container #description');
    var amount = document.querySelector('#smart-button-container #amount');
    var descriptionError = document.querySelector('#smart-button-container #descriptionError');
    var priceError = document.querySelector('#smart-button-container #priceLabelError');
    var invoiceid = document.querySelector('#smart-button-container #invoiceid');
    var invoiceidError = document.querySelector('#smart-button-container #invoiceidError');
    var invoiceidDiv = document.querySelector('#smart-button-container #invoiceidDiv');

    var elArr = [description, amount];

    if (invoiceidDiv.firstChild.innerHTML.length > 1) {
      invoiceidDiv.style.display = "block";
    }

    var purchase_units = [];
    purchase_units[0] = {};
    purchase_units[0].amount = {};

    function validate(event) {
      return event.value.length > 0;
    }

    paypal.Buttons({
      style: {
        color: 'gold',
        shape: 'pill',
        label: 'paypal',
        layout: 'vertical',
        
      },

      onInit: function (data, actions) {
        actions.disable();

        if(invoiceidDiv.style.display === "block") {
          elArr.push(invoiceid);
        }

        elArr.forEach(function (item) {
          item.addEventListener('keyup', function (event) {
            var result = elArr.every(validate);
            if (result) {
              actions.enable();
            } else {
              actions.disable();
            }
          });
        });
      },

      onClick: function () {
        if (description.value.length < 1) {
          descriptionError.style.visibility = "visible";
        } else {
          descriptionError.style.visibility = "hidden";
        }

        if (amount.value.length < 1) {
          priceError.style.visibility = "visible";
        } else {
          priceError.style.visibility = "hidden";
        }

        if (invoiceid.value.length < 1 && invoiceidDiv.style.display === "block") {
          invoiceidError.style.visibility = "visible";
        } else {
          invoiceidError.style.visibility = "hidden";
        }

        purchase_units[0].description = description.value;
        purchase_units[0].amount.value = amount.value;

        if(invoiceid.value !== '') {
          purchase_units[0].invoice_id = invoiceid.value;
        }
      },

      createOrder: function (data, actions) {
        return actions.order.create({
          purchase_units: purchase_units,
        });
      },

      onApprove: function (data, actions) {
        return actions.order.capture().then(function (orderData) {

          // Full available details
          console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));

          // Show a success message within this page, e.g.
          const element = document.getElementById('paypal-button-container');
          element.innerHTML = '';
          element.innerHTML = '<h3>Thank you for your payment!</h3>';

          // Or go to another URL:  actions.redirect('thank_you.html');
          
        });
      },

      onError: function (err) {
        console.log(err);
      }
    }).render('#paypal-button-container');
  }
  initPayPalButton();
  </script>
## CryptoCurrenciuees!
## ---------------------------------------Cryptos---------------------------------
## You can donate to the following Monero adress: 43UVoF1WP5UJeyGHCLF5xZV74aYovqTabMw8u6oGhQ4P5RzgR9LZr5cBSZGFpTwSGo7JHBQG7prnj4qAyjmKdX8SKwqxKVq
## You can also donate to the Bitcoin adress: 33za5vguhMQApqoyb8hQN3dx9u7jgdCh2r
### ------------------------I have other coins too:----------------------------
### Ethereum: 0xef7f69ce6886608ff07db8ae63b0f0ae7cbbba3c
### Dogecoin: DAJ6Uq2WoqXtLQq125Q8f5J8k1Mu4C3DUe
### Bitcoin Cash:qqnnywj2dywsc7mzxeecw2u862q72pllvv9vsqgtpg
### Tether: 0xef7f69ce6886608ff07db8ae63b0f0ae7cbbba3c
### Binance coin: bnb1g77wu63652mkh2drlgt3958dtpy82eznt3lafu
### Dash: XvzbEeZ7PH6KfgmC2AAdJNrP3vm2rbD9mM
### Ethereum Classic: 0xDe71Fc0f12a8Cf0bf391bc4474208178D776fcfC
#### -------------------------Below are paper wallets I don't recommend:-----------------------------
#### Litecoin: LZLi2P5fygMJFFMryrAz5TZinsUk1KHWxd
#### Zcash: t1cQkiH77o8gSMVjRrABjV3X7twdpyHVpfJ
#### Bytecoin: 23eBwK5hbrycWHcVHMVEHrivh61GuzY17HnXVafSKEmeEVZvadLbjYK5k2MHmUBgyPS8gpZY9WPf1EXWhqbj3KGsKPV9Z1q
#### digibyte: DEro1qXgTzCsLSUJUdPCuPqaz6ubTVfyoG
##### ------------------------Don't Use Ripple if you have other choices:-------------------------------------
##### Ripple: rMj1oE6iAzttXrahgNww5pSFNAiFYtRuFd
[back](https://qqiumax.github.io/home/)


