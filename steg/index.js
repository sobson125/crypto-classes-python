let imgdatauri;

function readURL(input) {
  if (input.files && input.files[0]) {
    let reader = new FileReader();

    reader.onload = function (e) {
      document.querySelector('#toBeEncoded').src = e.target.result;
      imgdatauri = e.target.result;
    };
  }
  reader.readAsDataURL(input.files[0]);
}

const decode = function (input) {
  if (input.files && input.files[0]) {
    let reader = new FileReader();

    reader.onload = function (e) {
      console.log(steg.decode(e.target.result));

      document.querySelector('#decoded').innerText = steg.decode(
        e.target.result
      );
    };
  }
  reader.readAsDataURL(input.files[0]);
};

const hideText = function () {
  document.querySelector('#encoded').src = steg.encode(
    document.querySelector('#text').value,
    imgdatauri
  );
};
