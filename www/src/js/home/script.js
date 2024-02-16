import get from 'lodash/get';

(async () => {
    let body = {
        msg: 'quarto script'
    };
    console.log(get(body, 'msg', 'nao_encontrado'));
})();