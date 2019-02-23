
let list = [];

function httpGetAsync(theUrl, callback) {
	const xmlHttp = new XMLHttpRequest();
	xmlHttp.onreadystatechange = function () {
		if (xmlHttp.readyState === 4 && xmlHttp.status === 200) { callback(xmlHttp.responseText); }
	};
	xmlHttp.open("GET", theUrl, true); // true for asynchronous
	xmlHttp.send(null);
}


function go(r) {

	// Turn the text file into an array, excluding the last empty string
	list = r.split("\n");
	list.pop();

	for (const item in list) {

		const parent = document.createElement("div");
		parent.className = "column is-half-mobile is-one-quarter-tablet is-2-desktop is-2-widescreen is-1-fullhd";

		const baby = document.createElement("img");
		baby.src = `../generator/out/drawable-xxxhdpi/${list[item]}`;
		baby.classList.add("inset");
		baby.classList.add("shadowed");

		parent.appendChild(baby);

		document.getElementById("box").appendChild(parent);
	}
}

httpGetAsync("iconList.txt", go);
