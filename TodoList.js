// let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
// let filter = 'all';

// function saveTasks() {
//   localStorage.setItem('tasks', JSON.stringify(tasks));
// }

// function renderTasks() {
//   const list = document.getElementById('taskList');
//   list.innerHTML = '';
//   let completedCount = 0;

//   const searchQuery = document.getElementById('searchInput')?.value.toLowerCase() || '';

//   tasks
//     .filter(task => {
//       if (filter === 'completed') return task.completed;
//       if (filter === 'pending') return !task.completed;
//       return true;
//     })
//     .filter(task => task.text.toLowerCase().includes(searchQuery))
//     .forEach((task, index) => {
//       const li = document.createElement('li');
//       if (task.completed) li.classList.add('completed');

//       const span = document.createElement('span');
//       span.textContent = `${task.text} (${task.priority})${task.dueDate ? ' - Due: ' + task.dueDate : ''}`;
//       span.onclick = () => toggleTask(index);

//       const editBtn = document.createElement('button');
//       editBtn.textContent = 'Edit';
//       editBtn.onclick = () => editTask(index);

//       const delBtn = document.createElement('button');
//       delBtn.textContent = 'Delete';
//       delBtn.onclick = () => deleteTask(index);

//       li.appendChild(span);
//       li.appendChild(editBtn);
//       li.appendChild(delBtn);
//       list.appendChild(li);

//       if (task.completed) completedCount++;
//     });

//   updateProgressBar(completedCount, tasks.length);
// }

// function addTask() {
//   const input = document.getElementById('taskInput');
//   const text = input.value.trim();
//   const priority = document.getElementById('priority').value;
//   const dueDate = document.getElementById('dueDate').value;

//   if (!text) return alert('Please enter a task');

//   tasks.push({ text, completed: false, priority, dueDate });
//   saveTasks();
//   renderTasks();
//   input.value = '';
//   document.getElementById('dueDate').value = '';
// }

// document.getElementById('taskInput').addEventListener('keypress', e => {
//   if (e.key === 'Enter') addTask();
// });

// function toggleTask(index) {
//   tasks[index].completed = !tasks[index].completed;
//   saveTasks();
//   renderTasks();
// }

// function editTask(index) {
//   const newText = prompt('Edit task:', tasks[index].text);
//   if (newText !== null && newText.trim() !== '') {
//     tasks[index].text = newText.trim();
//     saveTasks();
//     renderTasks();
//   }
// }

// function deleteTask(index) {
//   tasks.splice(index, 1);
//   saveTasks();
//   renderTasks();
// }

// function markAllDone() {
//   tasks.forEach(t => t.completed = true);
//   saveTasks();
//   renderTasks();
// }

// function deleteCompleted() {
//   tasks = tasks.filter(t => !t.completed);
//   saveTasks();
//   renderTasks();
// }

// function filterTasks(f) {
//   filter = f;
//   renderTasks();
// }

// function updateProgressBar(done, total) {
//   const percent = total === 0 ? 0 : (done / total) * 100;
//   document.getElementById('progressBar').style.width = `${percent}%`;
// }

// function toggleDarkMode() {
//   document.body.classList.toggle('dark-mode');
// }

// function sortByDate() {
//   tasks.sort((a, b) => (a.dueDate || '').localeCompare(b.dueDate || ''));
//   saveTasks();
//   renderTasks();
// }

// function sortByPriority() {
//   const priorityOrder = { high: 1, medium: 2, low: 3 };
//   tasks.sort((a, b) => priorityOrder[a.priority] - priorityOrder[b.priority]);
//   saveTasks();
//   renderTasks();
// }

// function searchTasks() {
//   renderTasks();
// }

// // Initial render
// renderTasks();




function addTask() {
  const input = document.getElementById('taskInput');
  const text = input.value.trim();
  if (!text) return;

  const li = document.createElement('li');
  li.innerHTML = `
    ${text}
    <button onclick="this.parentElement.remove()">Delete</button>
  `;

  document.getElementById('taskList').appendChild(li);
  input.value = '';
}
