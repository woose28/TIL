const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/data.txt";

const [romaNumber1, romaNumber2] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const romaToArabiaMapper = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
  IV: 4,
  IX: 9,
  XL: 40,
  XC: 90,
  CD: 400,
  CM: 900,
};

function convertToArabiaNumber(romaNumber) {
  let prevCharacter = "";

  let arabiaNumber = romaNumber
    .split("")
    .reduce((accArabiaNumber, romaCharacter) => {
      if (prevCharacter === "") {
        prevCharacter = romaCharacter;
        return accArabiaNumber;
      }

      const prevArabiaNumber = romaToArabiaMapper[prevCharacter];
      const curRomaNumber = romaToArabiaMapper[romaCharacter];

      if (prevArabiaNumber >= curRomaNumber) {
        prevCharacter = romaCharacter;
        return accArabiaNumber + prevArabiaNumber;
      }

      const exceptionArabiaNumber =
        romaToArabiaMapper[prevCharacter + romaCharacter];
      prevCharacter = "";

      return accArabiaNumber + exceptionArabiaNumber;
    }, 0);

  if (prevCharacter !== "") {
    arabiaNumber += romaToArabiaMapper[prevCharacter];
  }

  return arabiaNumber;
}

function convertToRomaNumber(arabiaNumber) {
  let romaNumber = "";
  let remainNumber = arabiaNumber;

  if (remainNumber >= 1000) {
    const MCharacterCount = Math.floor(remainNumber / 1000);

    romaNumber += "M".repeat(MCharacterCount);
    remainNumber = remainNumber % 1000;
  }

  if (remainNumber >= 900) {
    romaNumber += "CM";
    remainNumber -= 900;
  }

  if (remainNumber >= 500) {
    const DCharacterCount = Math.floor(remainNumber / 500);

    romaNumber += "D".repeat(DCharacterCount);
    remainNumber = remainNumber % 500;
  }

  if (remainNumber >= 400) {
    romaNumber += "CD";
    remainNumber -= 400;
  }

  if (remainNumber >= 100) {
    const CCharacterCount = Math.floor(remainNumber / 100);

    romaNumber += "C".repeat(CCharacterCount);
    remainNumber = remainNumber % 100;
  }

  if (remainNumber >= 90) {
    romaNumber += "XC";
    remainNumber = remainNumber - 90;
  }

  if (remainNumber >= 50) {
    const LCharacterCount = Math.floor(remainNumber / 50);

    romaNumber += "L".repeat(LCharacterCount);
    remainNumber = remainNumber % 50;
  }

  if (remainNumber >= 40) {
    romaNumber += "XL";
    remainNumber = remainNumber - 40;
  }

  if (remainNumber >= 10) {
    const XCharacterCount = Math.floor(remainNumber / 10);

    romaNumber += "X".repeat(XCharacterCount);
    remainNumber = remainNumber % 10;
  }

  if (remainNumber >= 9) {
    romaNumber += "IX";
    remainNumber = remainNumber - 9;
  }

  if (remainNumber >= 5) {
    const VCharacterCount = Math.floor(remainNumber / 5);

    romaNumber += "V".repeat(VCharacterCount);
    remainNumber = remainNumber % 5;
  }

  if (remainNumber >= 4) {
    romaNumber += "IV";
    remainNumber = remainNumber - 4;
  }

  if (remainNumber >= 1) {
    const ICharacterCount = Math.floor(remainNumber / 1);

    romaNumber += "I".repeat(ICharacterCount);
    remainNumber = remainNumber % 1;
  }

  return romaNumber;
}

const arabiaNumber1 = convertToArabiaNumber(romaNumber1);
const arabiaNumber2 = convertToArabiaNumber(romaNumber2);

const sumArabiaNumber = arabiaNumber1 + arabiaNumber2;
const sumRomaNumber = convertToRomaNumber(sumArabiaNumber);

console.log(sumArabiaNumber);
console.log(sumRomaNumber);
