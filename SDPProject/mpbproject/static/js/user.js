const pawnbrokersData = [
  {
    state: "Karnataka",
    city: "Bangalore",
    name: "ABC Pawnbrokers",
    address: "123 Main Street, Bangalore",
    phone: "123-456-7890"
  },
  {
    state: "Karnataka",
    city: "Mangalore",
    name: "XYZ Pawnbrokers",
    address: "456 Second Street, Mangalore",
    phone: "456-789-0123"
  },
  {
    state: "Maharashtra",
    city: "Mumbai",
    name: "PQR Pawnbrokers",
    address: "789 Third Street, Mumbai",
    phone: "789-012-3456"
  },
  {
    state: "Tamil Nadu",
    city: "Chennai",
    name: "LMN Pawnbrokers",
    address: "987 Fourth Street, Chennai",
    phone: "012-345-6789"
  },
  {
    state: "Andhra Pradesh",
    city: "Hyderabad",
    name: "EFG Pawnbrokers",
    address: "654 Fifth Street, Hyderabad",
    phone: "345-678-9012"
  }
];

const stateSelect = document.getElementById("state-select");
const citySelect = document.getElementById("city-select");
const submitButton = document.getElementById("submit-button");
const resultDiv = document.getElementById("result");

// Populate cities based on selected state
stateSelect.addEventListener("change", e => {
  const selectedState = e.target.value;
  const cities = pawnbrokersData
    .filter(data => data.state === selectedState)
    .map(data => data.city);
  citySelect.innerHTML = `<option value="" disabled selected>Select a city</option>`;
  cities.forEach(city => {
    const option = document.createElement("option");
    option.value = city;
    option.text = city;
    citySelect.appendChild(option);
  });
});

// Show pawnbroker details based on selected state and city
const showDetails = () => {
  const selectedState = stateSelect.value;
  const selectedCity = citySelect.value;
  const pawnbroker = pawnbrokersData.find(data => data.state === selectedState && data.city === selectedCity);
  if (pawnbroker) {
    resultDiv.innerHTML = `
      <p><strong>Name:</strong> ${pawnbroker.name}</p>
      <p><strong>Address:</strong> ${pawnbroker.address}</p>
      <p><strong>Phone:</strong> ${pawnbroker.phone}</p>
    `;
  } else {
    resultDiv.innerHTML = "<p>No pawnbroker found in the selected location</p>";
  }
}

// Handle submit button click event
submitButton.addEventListener("click", showDetails);
