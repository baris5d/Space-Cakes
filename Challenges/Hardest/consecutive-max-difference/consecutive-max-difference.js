// Parameter array is an array of integers
// The function should return an integer
function consecutiveMaxDifference(array) {
	array = array.sort((a, b) => a - b);
	max = 0;
	for(let i = 0; i < array.length - 1; ++i) {
		max = Math.max(max, array[i + 1] - array[i]);
	}
	return max;
}
