let temp = "CTFITB{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}";
let flag = [
  65, 52, 22, 226, 178, 3, 137, 249, 54, 19, 41, 244, 148, 114, 132, 195, 104,
  53, 35, 223, 185, 52, 129, 217, 93, 80, 62, 199, 215, 47, 183, 195, 102, 5,
  96, 201, 128, 20, 129, 255, 58, 47, 2, 244, 174, 32, 154, 253, 35, 29,
];
let randoms = [];
let final_flag = [];
for (let i = 0; i < "CTFITB{".length; i++) {
  randoms.push(flag[i] ^ temp.charCodeAt(i));
}
// randoms.push(80);
console.log(randoms);
for(let j=0;j<256;j++){
  randoms.push(j)
  // rem = []
  for (let i = 0; i < temp.length; i++) {
    // if (i==0 ||  ((i+1) % 8) !== 0) {
      final_flag.push(String.fromCharCode(randoms[i % 8] ^ flag[i]));
    // } else {
    //   rem.push(flag[i])
    //   final_flag.push("~");
    // }
  }
  // console.log(rem)
  if(final_flag[7].charCodeAt(0)<127 && final_flag[7].charCodeAt(0) > 32){
    console.log(final_flag.join(""));
  }
  final_flag = []
  randoms.pop()

}

