document.addEventListener("DOMContentLoaded", () => {
  // Function to load JSON data and populate the form
  function loadData() {
    let jsonData = JSON.parse(localStorage.getItem("pandoraData")) || [];

    if (jsonData.length > 0) {
      // Populate the form with the first item in the JSON data
      document.getElementById("season").value = jsonData[0]["Season"];
      document.getElementById("year").value = jsonData[0]["Year"];
      document.getElementById("releases").value = jsonData[0]["Releases"];
    }

    // Populate the table with all the JSON data
    const tableBody = document.querySelector("#data-table tbody");
    tableBody.innerHTML = ""; // Clear existing table rows
    jsonData.forEach((item) => {
      const row = document.createElement("tr");
      const seasonCell = document.createElement("td");
      const yearCell = document.createElement("td");
      const releasesCell = document.createElement("td");
      seasonCell.textContent = item.Season;
      yearCell.textContent = item.Year;
      releasesCell.textContent = item.Releases;
      row.appendChild(seasonCell);
      row.appendChild(yearCell);
      row.appendChild(releasesCell);
      tableBody.appendChild(row);
    });
  }

  // Function to save data to local storage
  function saveData(data) {
    let jsonData = JSON.parse(localStorage.getItem("pandoraData")) || [];
    jsonData.push(data);
    localStorage.setItem("pandoraData", JSON.stringify(jsonData));
  }

  // Attach event listener to the load data button
  document.getElementById("loadDataButton").addEventListener("click", loadData);

  // Handle form submission
  document
    .getElementById("jewelryForm")
    .addEventListener("submit", function (event) {
      event.preventDefault();

      const formData = new FormData(event.target);
      const data = {};
      formData.forEach((value, key) => {
        data[key] = value;
      });

      saveData(data); // Save the data to local storage

      // Optionally add the new data to the table
      const tableBody = document.querySelector("#data-table tbody");
      const row = document.createElement("tr");
      const seasonCell = document.createElement("td");
      const yearCell = document.createElement("td");
      const releasesCell = document.createElement("td");
      seasonCell.textContent = data.season;
      yearCell.textContent = data.year;
      releasesCell.textContent = data.releases;
      row.appendChild(seasonCell);
      row.appendChild(yearCell);
      row.appendChild(releasesCell);
      tableBody.appendChild(row);

      // Clear the form
      event.target.reset();
    });

  // Load data on page load
  loadData();
});
