/*
  shows a popup of text when the cite button is clicked
*/


function toggleByHref(anchor) {
  event.preventDefault(); // prevent jumping to the id
  const targetId = anchor.getAttribute("href").replace("#", "");
  const target = document.getElementById(targetId);
  if (target) {
    target.classList.toggle("citation-hidden");
  }
}
