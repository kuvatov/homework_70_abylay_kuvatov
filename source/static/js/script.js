textarea = document.querySelector('textarea');
  if(textarea){
    textarea.addEventListener('input', autoResize, false);
    textarea.addEventListener('click', autoResize, false);
  }

    function autoResize() {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    }
