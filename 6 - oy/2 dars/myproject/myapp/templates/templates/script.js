function showView(viewName) {
    const views = document.querySelectorAll('.view');
    views.forEach(view => view.style.display = 'none');

    const selectedView = document.getElementById(viewName);
    if (selectedView) {
        selectedView.style.display = 'block';
    }
}
