<html>
<head>
<script src="https://cdn.jsdelivr.net/npm/p5@1.4.0/lib/p5.js"></script>
<script>
  function setup() {
  createCanvas(1500, 1500);
}

function draw() {
  if (mouseIsPressed) {
    fill(0);
  } else {
    fill(255);
  }
  ellipse(mouseX, mouseY, 80, 80);
}
</script>
</head>
<body>
<h1>John's Awesome Drawing Space...</h1>
<main></main>
<hr/>

</body>
</html>