for (let i = 1; i <= 100; ++i) {
  if (i % 3 == 0 || String(i).includes("3")) {
    console.log(i, "(アホ)");
  } else {
    console.log(i);
  }
}