// Carrega os itens salvos quando a página é carregada
document.addEventListener('DOMContentLoaded', () => {
    loadItems();
});

// Array para armazenar os itens
let items = JSON.parse(localStorage.getItem('items')) || [];

// Referências aos elementos DOM
const itemForm = document.getElementById('itemForm');
const itemInput = document.getElementById('itemInput');
const itemList = document.getElementById('itemList');

// Adicionar novo item
itemForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const itemText = itemInput.value.trim();
    
    if (itemText) {
        addItem(itemText);
        itemInput.value = '';
        saveItems();
        loadItems();
    }
});

// Função para adicionar item
function addItem(text) {
    items.push({
        id: Date.now(),
        text: text,
        completed: false
    });
}

// Função para salvar itens no localStorage
function saveItems() {
    localStorage.setItem('items', JSON.stringify(items));
}

// Função para carregar e exibir itens
function loadItems() {
    itemList.innerHTML = '';
    items.forEach(item => {
        const li = document.createElement('li');
        li.innerHTML = `
            <span class="${item.completed ? 'completed' : ''}">${item.text}</span>
            <div class="buttons">
                <button onclick="toggleItem(${item.id})" class="toggle">
                    ${item.completed ? '✓' : '◯'}
                </button>
                <button onclick="editItem(${item.id})" class="edit">✎</button>
                <button onclick="deleteItem(${item.id})" class="delete">✖</button>
            </div>
        `;
        itemList.appendChild(li);
    });
}

// Função para alternar estado do item (completado/não completado)
function toggleItem(id) {
    items = items.map(item => {
        if (item.id === id) {
            return { ...item, completed: !item.completed };
        }
        return item;
    });
    saveItems();
    loadItems();
}

// Função para editar item
function editItem(id) {
    const item = items.find(item => item.id === id);
    const newText = prompt('Editar item:', item.text);
    
    if (newText !== null) {
        items = items.map(item => {
            if (item.id === id) {
                return { ...item, text: newText.trim() };
            }
            return item;
        });
        saveItems();
        loadItems();
    }
}

// Função para deletar item
function deleteItem(id) {
    if (confirm('Tem certeza que deseja excluir este item?')) {
        items = items.filter(item => item.id !== id);
        saveItems();
        loadItems();
    }
}