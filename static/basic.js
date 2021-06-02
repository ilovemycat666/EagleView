// var hangars = ['KRVS', 'CYYT', 'CYOW', '00C', 'KMFE', 'KGXY', 'KGXY', 'KLZU', 'KADS ', 'KLFT ', 'CYXC', 'CYYT', 'CYOW', 'CYQY', 'KFCM', 'KMGY', 'KDRO', 'KAVP', 'KPLU', 'KSNY', 'KFCM', 'KBFF', 'PHJR (JRF)', 'KFDK', 'KSXK', 'KEKO', 'CYXE', 'PHOG (OGG)', 'KJAN', 'KHKY', 'KLNK', 'KSBN', 'KAEG', 'KLYH', 'CYWG', 'KOLM', 'KGKY', 'KHEF', 'CZVL', 'KDPA', 'KRIL', 'KTVC', 'KOJC', 'KROC', 'KPIH', 'KPVU', 'KGTU', 'KYKM', 'KIDA', 'KCMI', 'KCOE', 'KBJC', 'KFNL', 'KCXY', 'KJKJ', 'PHKO (KOA)', 'KHLN', 'KDLH', 'KABR', 'KMAF', 'KFAR', 'KRBW', 'KMRT', 'CYLW', 'KEUG', 'KSTS', 'KLBE', 'KIKV', 'KRNO', 'KSGU', 'KGCN', 'KBKV', 'KBLI', 'KRDM', 'KHDC', 'CYQB', 'KSTC', 'KRME', 'CYHZ', 'KFMN'];
var colors = ['#a2b9bc', '#b2ad7f', '#878f99', '#6b5b95', '#6b5b95', '#feb236', '#d64161', '#ff7b25', '#eca1a6', '#bdcebe', '#ada397', '#d5e1df', '#e3eaa7', '#b5e7a0', '#86af49', '#b9936c', '#dac292', '#e6e2d3', '#c4b7a6', '#3e4444', '#82b74b', '#405d27', '#c1946a', '#92a8d1', '#034f84', '#f7cac9', '#f7786b', '#b1cbbb', '#eea29a', '#c94c4c', '#d5f4e6', '#80ced6', '#fefbd8', '#618685', '#ffef96', '#50394c', '#b2b2b2', '#f4e1d2', '#fefbd8', '#618685', '#36486b', '#4040a1', '#b2b2b2', '#f4e1d2', '#f18973', '#bc5a45', '#f0f0f0', '#c5d5c5', '#9fa9a3', '#e3e0cc', '#eaece5', '#b2c2bf', '#c0ded9', '#e4d1d1', '#b9b0b0', '#d9ecd0', '#77a8a8', '#f0efef', '#ddeedd', '#c2d4dd', '#b0aac0', '#c8c3cc', '#563f46', '#8ca3a3', '#484f4f', '#e0e2e4', '#c6bcb6', '#96897f', '#625750', '#7e4a35', '#cab577', '#dbceb0', '#838060', '#bbab9b', '#8b6f47', '#d4ac6e', '#4f3222', '#686256', '#c1502e', '#587e76', '#a96e5b', '#454140', '#bd5734', '#a79e84', '#7a3b2e', '#bccad6', '#8d9db6', '#667292', '#f1e3dd', '#cfe0e8', '#b7d7e8', '#87bdd8', '#daebe8', '#fbefcc', '#f9ccac', '#f4a688', '#e0876a', '#fff2df', '#d9ad7c', '#a2836e', '#674d3c', '#f9d5e5', '#eeac99', '#e06377', '#c83349', '#5b9aa0', '#d6d4e0', '#b8a9c9', '#622569', '#96ceb4', '#ffeead', '#ffcc5c', '#ff6f69', '#588c7e', '#f2e394', '#f2ae72', '#d96459'];


function colorized (hangars){
	for (i in hangars) {
		var them = document.getElementsByClassName(hangars[i]);
		for (j=0; j < them.length; j++) {
			them[j].style.backgroundColor = colors[i];
		}
	}
	var means = document.getElementsByClassName('xbar');
	for (i=0; i<means.length;i++) {
		if (parseInt(means[i].innerHTML.slice(3)) > 4.5) {
			means[i].parentElement.style.display = 'none';
		}
	}
}



function average() {
	var select = document.getElementById('average');
	console.log(select.value)
	var means = document.getElementsByClassName('xbar');
	for (i=0; i<means.length;i++) {
		if (parseInt(means[i].innerHTML.slice(3)) > parseInt(select.value)) {
			means[i].parentElement.style.display = 'none';
		}
		else if (parseInt(means[i].innerHTML.slice(3)) <= parseInt(select.value)) {
			means[i].parentElement.style.display = 'inline';
		}
	}
}