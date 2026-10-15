const fs = require("fs");
const src = fs.readFileSync("i18n.js", "utf8");
const cut = src.indexOf("(function () {");
const head = src.slice(0, cut) + "\nmodule.exports = { CQ_LANGS, CQ_T };";
fs.writeFileSync("_i18n_eval.js", head);
const { CQ_LANGS, CQ_T } = require("./_i18n_eval.js");
const codes = Object.keys(CQ_T);
const base = Object.keys(CQ_T.en);
let ok = true;
codes.forEach(c => {
  const miss = base.filter(k => !(k in CQ_T[c]));
  const extra = Object.keys(CQ_T[c]).filter(k => !base.includes(k));
  if (miss.length || extra.length) {
    ok = false;
    console.log(c, "MISSING:", miss.join(","), "| EXTRA:", extra.join(","));
  }
  if (Array.isArray(CQ_T[c].gchip) && CQ_T[c].gchip.length !== CQ_T.en.gchip.length)
    console.log(c, "gchip len:", CQ_T[c].gchip.length);
});
console.log("langs:", codes.length, "| en keys:", base.length, "|", ok ? "ALL KEYS PRESENT" : "GAPS FOUND");
fs.unlinkSync("_i18n_eval.js");
