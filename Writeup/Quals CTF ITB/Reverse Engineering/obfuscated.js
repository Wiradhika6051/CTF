//return niulai di list fungsi pada indeks a - 340
function func1(a, b) {
  const lists = get_functions();
  return (
    (func1 = function (arg1, arg2) {
      arg1 = arg1 - 340;
      let func = lists[arg1];
      return func;
    }),
    func1(a, b) 
  );
}
//helper == func1
const helper = func1;

// const function_list = [
//0   "prototype",
//1   "console",
//2   "1426432jlZlon",
//3   "24NcLsad",
//4   "search",
//5   "1437704cGeqiZ",
//6   "9MGLQiz",
//7   "__proto__",
//8   "1488Eulffi",
//9   "warn",
//10   "trace",
//11   "toString",
//12   "33wuVVmu",
//13   "log",
//14   "185482euNCIu",
//15   "8006889AWsaHN",
//16   "436163oydeiG",
//17   "bind",
//18   "10xVPXyQ",
//19   "floor",
//20   "length",
//21   "table",
//22   "15220632zgoPdm",
//23   "exception",
//24   "constructor",
//25   "39KSIZml",
//26   "(((.+)+)+)+$",
//27   "20755eGwtzy",
// ];
//pemanggilan awla
(function (args1, args2) {
  const f1 = func1,
    f2 = args1(); //f2 == daftar fungsi
  while (!![]) { //while true
    try {//340
      const res =
        parseInt(f1(340)) / 1 +  //lists[0] = prototype
        (-parseInt(f1(366)) / 2) * //lists[26]
          (-parseInt(f1(364)) / 3) +//lists[24]
        (-parseInt(f1(360)) / 4) *//lists[20]
          (-parseInt(f1(351)) / 5) +//lists[11]
        (parseInt(f1(355)) / 6) *//lists[15]
          (parseInt(f1(354)) / 7) +//lists[14]
        (-parseInt(f1(357)) / 8) *//lists[17]
          (-parseInt(f1(358)) / 9) +//lists[18]
        (parseInt(f1(342)) / 10) *//lists[2]
          (parseInt(f1(367)) / 11) +//lists[27]
        (-parseInt(f1(346)) / 12) *//lists[26]
          (parseInt(f1(349)) / 13);//lists[9]
      if (res === args2) break;
      else f2["push"](f2["shift"]());
    } catch (error) {
      f2["push"](f2["shift"]());
    }

    //valdi:
//     1426432jlZlon , 1426432
// 24NcLsad , 24
// 1437704cGeqiZ , 1437704
// 9MGLQiz , 9
// 1488Eulffi , 1488
// 33wuVVmu , 33
// 185482euNCIu , 185482
// 8006889AWsaHN , 8006889
// 436163oydeiG , 436163
// 10xVPXyQ , 10
// 15220632zgoPdm , 15220632
// 39KSIZml , 39
// 20755eGwtzy , 20755
  }
})(get_functions, 0xe021c);

const final_array = [
  "436163oydeiG",
  "bind",
  "10xVPXyQ",
  "floor",
  "length",
  "table",
  "15220632zgoPdm",
  "exception",
  "constructor",
  "39KSIZml",
  "(((.+)+)+)+$",
  "20755eGwtzy",
  "prototype",
  "console",
  "1426432jlZlon",
  "24NcLsad",
  "search",
  "1437704cGeqiZ",
  "9MGLQiz",
  "__proto__",
  "1488Eulffi",
  "warn",
  "trace",
  "toString",
  "33wuVVmu",
  "log",
  "185482euNCIu",
  "8006889AWsaHN"
]
let MIN = 0,
  MAX = 255;
function generate() {
  const v1 = func1,
    v2 = (function () {
      let v3 = !![];//true
      return function (p1, p2) {
        const v4 = v3 //true
          ? function () {
              if (p2) {
                const v5 = p2["apply"](p1, arguments);
                return (p2 = null), v5;
              }
            }
          : function () {};
        return (v3 = ![]), v4;
      };
    })(),
    /*
    v2 = function (p1, p2) {
        const v4 = v3 //true
          ? function () {
              if (p2) {
                const v5 = p2["apply"](p1, arguments);
                return (p2 = null), v5;
              }
            }
          : function () {};
        return (v3 = ![]), v4; -> (v3 = false), v4 -> if(v6...){}
      };
    */
    v6 = v2(this, function () {
      const v7 = func1; //get [a-340]
      return v6["toString"]()
        ["search"](v7(350)) //10 ->'(((.+)+)+)+$'
        [v7(363)]() //23 -> 'toString'()
        [v7(348)](v6) //8 -> 'constructor' (v6)
        [v7(356)](v7(350)); //16, 10 ->'search'('(((.+)+)+)+$')
        //return:
        //v6.toString().search('(((.+)+)+)+$').toString().constructor(v6).search('(((.+)+)+)+$')
        //->true
    });
  v6(); //asumsi true
  const v8 = (function () {
      let v9 = !![]; //true
      return function (pa1, pa2) {
        const v10 = v9
          ? function () {
              if (pa2) {
                const v11 = pa2["apply"](pa1, arguments);
                return (pa2 = null), v11;
              }
            }
          : function () {};
        return (v9 = ![]), v10;
      };
    })(),
    v12 = v8(this, function () {
      const v13 = func1,
        v14 = function () {
          let v15;
          try {
            v15 = Function(
              "return\x20(function()\x20" +
                "{}.constructor(\x22return\x20this\x22)(\x20)" +
                ");"
            )();
          } catch (e) {
            v15 = window;
          }
          console.log(v15)
          return v15;
        },
        v16 = v14(),
        v17 = (v16[v13(0x161)] =
          v16[v13(0x161)] || {}),
        list = [
          v13(365),
          v13(0x169),
          "info",
          "error",
          v13(0x15b),
          v13(0x159),
          v13(0x16a),
        ];
      for (
        let i = 0;
        i < list[v13(344)]; // func1[4] -> length
        i++
      ) {
        const v19 =
            v8["constructor"][v13(352)][v13(341)](
              v8
            ),
          v20 = list[i],
          v21 = v17[v20] || v19;
        (v19[v13(359)] = v8["bind"](v8)),
          (v19[v13(363)] =
            v21["toString"][v13(341)](v21)),
          (v17[v20] = v19);
      }
    });
  return (
    // v12(),
    Math[v1(0x157)](Math["random"]() * (MAX - MIN + 0x1) + MIN)
  );
}
function get_functions() {
  const function_list = [
    "prototype",
    "console",
    "1426432jlZlon",
    "24NcLsad",
    "search",
    "1437704cGeqiZ",
    "9MGLQiz",
    "__proto__",
    "1488Eulffi",
    "warn",
    "trace",
    "toString",
    "33wuVVmu",
    "log",
    "185482euNCIu",
    "8006889AWsaHN",
    "436163oydeiG",
    "bind",
    "10xVPXyQ",
    "floor",
    "length",
    "table",
    "15220632zgoPdm",
    "exception",
    "constructor",
    "39KSIZml",
    "(((.+)+)+)+$",
    "20755eGwtzy",
  ];
  get_functions = function () {
    return function_list;
  };
  return get_functions(); //return daftar fungsi (array)
}
let flag = "CTFITB{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}",
  randoms = [];
for (let i = 0; i < 8; i++) {
  randoms["push"](generate());
}
for (let i = 0; i < flag[helper(344)]; i++) {
  console[helper(365)](flag[i] ^ randoms[i % 8]);
}
