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



/**
 * Definition for singly-linked list.
 *
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 *
 * @param {ListNode} head
 * @returns {boolean}
 */
function hasCycle(head) {
  if (head === null) {
    return false;
  }

  let slow = head;
  let fast = head;

  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;

    if (slow === fast) {
      return true;
    }
  }

  return false;
}


/**
 * Definition for singly-linked list.
 *
 * function ListNode(val) {
 *   this.val = val
 *   this.next = null
 * }
 *
 * @param {ListNode} head
 * @returns {ListNode}
 */
function findMiddleListNode(head) {
  let slow = head;
  let fast = head;

  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
  }

  return slow;
}

/**
 * Definition for singly-linked list.
 *
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 *
 * @param {ListNode} node
 * @returns {void} Do not return anything, modify node in-place instead.
 */

function deleteNode(node) {
  node.val = node.next.val;
  node.next = node.next.next;
}



/**
 * Definition for singly-linked list.
 *
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 *
 * @param {ListNode} head
 *
 * @returns {ListNode}
 */
function reverseList(head) {
  let prev = null;
  let curr = head;

  while (curr !== null) {
    const next = curr.next;

    curr.next = prev;

    prev = curr;
    curr = next;
  }

  return prev;
}


/**
 * @param val
 * @constructor
 */
function ListNode(val) {
  this.val = val;
  this.next = null;
}

/**
 * Merges two sorted linked lists and returns the merged sorted list.
 *
 * @param {ListNode} l1 - First sorted linked list.
 * @param {ListNode} l2 - Second sorted linked list.
 * @returns {ListNode} - Merged sorted linked list.
 */
function mergeTwoLists(l1, l2) {
  // Create a dummy node to simplify edge cases.
  const dummy = new ListNode(-1);
  let current = dummy;

  // Traverse both lists while both are non-empty.
  let p1 = l1;
  let p2 = l2;

  while (p1 !== null && p2 !== null) {
    if (p1.val < p2.val) {
      current.next = p1;
      p1 = p1.next;
    } else {
      current.next = p2;
      p2 = p2.next;
    }
    current = current.next;
  }

  // If either list is non-empty, append it to the result.
  if (p1 !== null) {
    current.next = p1;
  } else {
    current.next = p2;
  }

  // Return the merged list, skipping the dummy node.
  return dummy.next;
}


class Stack {
  constructor() {
    this.items = [];
  }

  /**
   * Add value to the stack
   * @param {number} value
   *
   * @returns {void}
   */
  push(value) {
    this.items.push(value);
  }

  /**
   * Return stack size
   *
   * @returns {number}
   */
  size() {
    return this.items.length;
  }

  /**
   * Return the last added value
   *
   * @returns {number|null}
   */
  peek() {
    return this.items.length ? this.items[this.items.length - 1] : null;
  }

  /**
   * Return the last added value and remove it from the stack
   *
   * @returns {number|null}
   */
  pop() {
    return this.items.length ? this.items.pop() : null;
  }

  /**
   * Empty the stack
   *
   * @returns {void}
   */
  clear() {
    this.items = [];
  }

  /**
   * Serialize the stack
   *
   * @returns {number[]}
   */
  serialize() {
    return [...this.items].reverse();
  }

  /**
   * Check if the stack is empty
   *
   * @returns {boolean}
   */
  isEmpty() {
    return this.items.length === 0;
  }
}


function countQueueTime(customers, n) {
  if (n === 1) {
    return customers.reduce((acc, curr) => acc + curr, 0);
  }

  const machines = Array(n).fill(0);

  for (const time of customers) {
    machines.sort((a, b) => a - b);
    machines[0] += time;
  }

  return Math.max(...machines);
}
