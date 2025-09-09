function normalizeName(name) {
  // "Katherine Johnson" -> "katherinejohnson"
  return name.replace(/\s+/g, "_").toLowerCase(); 
}

export function getImageUrl(person) {
  console.log(`./${normalizeName(person.name)}.png`)
  return `./${normalizeName(person.name)}.png`;
}
