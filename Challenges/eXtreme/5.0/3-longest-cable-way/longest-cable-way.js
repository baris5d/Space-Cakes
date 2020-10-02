// Örnek veriler
var exampleInputs = [
	'444\n16 2\n3 2\n2 2\n30 3\n50 10\n45 12\n8 12\n0 0',
	'44\n30 31\n50 10\n45 12\n90 21\n43 1\n0 0'
];

// Input değerlerini parsela (yapacağımız işlemle alakasız sadece test ortamı için kolaylık yaratmak için yazdım)
function parseInput(stdin) {
	stdin = stdin.split('\n');

	const total = parseInt(stdin.shift());

	let values = [];
	while(input = (stdin.length) ? stdin.shift().split(' ') : false) {

		// Syntax garip gözükebilir, şu işlemin kısaltılmış halini yapıyor
		// var V = parseInt(input[0]); var Count = parseInt(input[1]);
		[V, Count] = [parseInt(input[0]), parseInt(input[1])];

		// Array'i değer için belirlenen adet kadar doldur ve birleştir
		values = values.concat(new Array(Count).fill(V));
	}

	// Büyükten küçüğe doğru sırala
	values = values.sort((a, b) => b - a);

	return [total, values]
}



// Örnek verileri işleme sok
for(stdin of exampleInputs) {

	[target, parts] = parseInput(stdin);

	let answer = findLeastJointedWay(target, parts);
	console.log(answer);

}

function findLeastJointedWay(target, parts) {

	    // let foundCombinations = []; // DEBUG için

		let minJoints = Infinity; // Sonucumuz bu olacak (Infinity JS'de her sayıdan büyük olduğu için verebileceğim en büyük max değer bu)

		let leastValue = parts[parts.length - 1];
		if(leastValue > target) {
			// En düşük değer hedeften büyükse direkt bitiriyoruz işlemi
			return "No solution possible"; // Bkz. 3.4
		}

		// İlk önce en büyük değeri baz alarak, onun ilerisindeki tüm değerleri tek tek geziyoruz
		for(let i = 0; i < parts.length; ++i) {

			let currentCombination = [];

			let sum = parts[i];
			currentCombination.push(parts[i]);

			if(sum > target) {
				continue; // İlk değerimiz hedeften büyükse bekleme yapma devam et
			} else if (sum == target) {
				return 0; // Eğer tek değerle hedefe ulaştıysak, hiç birleşme yeri olmadığı için cevap 0
			}

			// Baz aldığımız değerin ilerisindeki tüm değerleri alıp
			// Eğer toplama eklersek hedefi ulaştık mı yoksa devam mı etmeliyiz diye kontrol ediyoruz
			for(let j = i + 1; j < parts.length; ++j) {

				let V = parts[j];

				// Hedefin hala altındaysak veya eşitsek
				if(V + sum <= target) {
					sum += V; // Toplamı arttır ve ...
					currentCombination.push(V); // Şu anki değeri komibinasyona ekle
				}

				if (sum == target) {
					// Sonuca ulaşmışsak döngüyü kır, diğer sonuçları işleme sokmaya gerek kalmadı
					break;
				}

			}

			// Hedefe ulaştıysak
			if(sum == target) {
				// Sonucu şimdiki değer ile karşılaştır, en küçüğü bul
				minJoints = Math.min(minJoints, currentCombination.length - 1);
				// foundCombinations.push(currentCombination); // DEBUG için
			}
		}

		// Bkz. 3.4
		return minJoints == Infinity ? "No solution possible" : minJoints;

		// DEBUG için
		/* foundCombinations.forEach(x => console.log({
			combination: x, // Kombinasyon
			parts: x.length, // Parça sayısı
			joints: x.length - 1 // Birleştirme köşesi / Eklem (Joint) sayısı
			})
		); */
}
