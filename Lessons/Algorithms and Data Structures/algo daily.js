/**
 * @param {number} x
 *
 * @returns {number}
 */
function sqrt(x) {
  if (x < 2) {
    return x;
  }

  let left = 2;
  let right = Math.floor(x / 2);

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const num = mid * mid;

    if (num === x) {
      return mid;
    } else if (num < x) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return right;
}


/**
 * @param {number[]} arr
 *
 * @returns {number}
 */
function peakIndexInMountainArray(arr) {
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] < arr[mid + 1]) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  return left;
}


function countNegatives(grid) {
  let count = 0;
  const rows = grid.length;
  const cols = grid[0].length;
  let row = 0;
  let col = cols - 1;

  while (row < rows && col >= 0) {
    if (grid[row][col] < 0) {
      count += rows - row;
      col--;
    } else {
      row++;
    }
  }

  return count;
}




class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  /**
   * Add value to the end of the list
   * @param {number} value
   * @returns {void}
   */
  append(value) {
    const newNode = new Node(value);

    if (this.isEmpty()) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.length++;
  }

  /**
   * Add value to the beginning of the list
   * @param {number} value
   * @returns {void}
   */
  prepend(value) {
    const newNode = new Node(value);

    if (this.isEmpty()) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.next = this.head;
      this.head = newNode;
    }
    this.length++;
  }

  /**
   * Return list size
   * @returns {number}
   */
  size() {
    return this.length;
  }

  /**
   * Return whether list is empty
   * @returns {boolean}
   */
  isEmpty() {
    return this.length === 0;
  }

  /**
   * Return the last node's value
   * @returns {number|null}
   */
  getLast() {
    return this.tail ? this.tail.value : null;
  }

  /**
   * Return the first node's value
   * @returns {number|null}
   */
  getFirst() {
    return this.head ? this.head.value : null;
  }

  /**
   * Empty the list
   * @returns {void}
   */
  clear() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  /**
   * Delete node by its value
   * @param {number} value
   * @returns {void}
   */
  delete(value) {
    if (this.isEmpty()) {
      return;
    }

    // Handle deletion of head
    if (this.head.value === value) {
      this.head = this.head.next;

      if (!this.head) {
        this.tail = null;
      }
      this.length--;

      return;
    }

    // Handle deletion of nodes other than head
    let currentNode = this.head;

    while (currentNode.next && currentNode.next.value !== value) {
      currentNode = currentNode.next;
    }

    if (currentNode.next) {
      currentNode.next = currentNode.next.next;

      if (!currentNode.next) {
        this.tail = currentNode;
      }
      this.length--;
    }
  }

  /**
   * Serialize the list
   * @returns {number[]}
   */
  serialize() {
    const values = [];
    let currentNode = this.head;

    while (currentNode) {
      values.push(currentNode.value);
      currentNode = currentNode.next;
    }

    return values;
  }
}
