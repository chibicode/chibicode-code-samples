var linkedList1 = {
  text: 'A',
  next: { text: 'B', next: null }
}

var linkedList2 = {
  text: 'A',
  next: {
    text: 'B',
    next: {
      text: 'C',
      next: {
        text: 'D',
        next: null
      }
    }
  }
}

// Do not create a new object
// Do not create a new array
// Do not add additional keys
function reverseLinkedList(linkedList) {
  let before = null
  let current = linkedList
  let after
  while (current) {
    after = current['next']
    current['next'] = before
    before = current
    current = after
  }
  return before
}

// {"text":"B","next":{"text":"A","next":null}}
console.log(JSON.stringify(reverseLinkedList(linkedList1)))

// {"text":"D","next":{"text":"C","next":{"text":"B","next":{"text":"A","next":null}}}}
console.log(JSON.stringify(reverseLinkedList(linkedList2)))
