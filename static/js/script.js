document.addEventListener('DOMContentLoaded', () => {
    console.log('Stokki Dashboard Loaded');
    

    const actionBtns = document.querySelectorAll('.action-btn');
    actionBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            console.log('Action clicked:', btn.textContent.trim());
        });
    });
});
