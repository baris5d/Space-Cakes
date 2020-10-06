function is_Palindrome(wrd) {
    var reverse = wrd.split("").reverse().join("");
    return wrd == reverse;
}

function longest_palindrome(dct) {

    var max_length = 0,
        maxp = '';

    for (var i = 0; i < dct.length; i++) {
        var subs = dct.substr(i, dct.length);

        for (var j = subs.length; j >= 0; j--) {
            var sub_subs_str = subs.substr(0, j);
            if (sub_subs_str.length <= 1)
                continue;

            if (is_Palindrome(sub_subs_str)) {
                if (sub_subs_str.length > max_length) {
                    max_length = sub_subs_str.length;
                    maxp = sub_subs_str;
                }
            }
        }
    }

    return maxp;
}

console.log(longest_palindrome("algorithmsforhacktoberfest2019"));