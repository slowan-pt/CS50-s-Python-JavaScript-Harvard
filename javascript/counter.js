let count = 0;
            function countermais() {
                count++;
                document.querySelector('h1').innerHTML = 'contador: ' + count;
              
                if (count % 10 === 0) {
                alert(`Contador é um múltiplo de 10: ${count}`);
                }
            }
            function countermenos() {
                count--;
                document.querySelector('h1').innerHTML = 'contador: ' + count;

                if (count % 10 === 0) {
                alert(`Contador é um múltiplo de 10: ${count}`);
                document.addEventListener('DomContentLoaded', function() {
                    document.querySelector('h1').innerHTML = 'contador: ' + count;
                });
            }
            }

            document.querySelector('button').onclick = count;
