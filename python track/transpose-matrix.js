/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var transpose = function(matrix) {
    var m = [];
    for (i =0;i < matrix[0].length;i++){
        var x = [];
        for (j = 0;j<matrix.length;j++){
            x.push(matrix[j][i]);
        }
        m.push(x);

    }
    return m;
};