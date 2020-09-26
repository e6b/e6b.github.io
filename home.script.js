
var wlcQuotes = 'You can write me down in history with hateful, twisted lies, you can tread me in this very dirt, but still, like dust, I\'ll rise.--Maya Angelou';
let dom = document.querySelector('#root');


let elementP70 = React.createElement(
    'div', {}, [
    React.createElement(
        'p', {}, wlcQuotes
    ),
    React.createElement('h2', {}, 'MY READING LISTS'),
    React.createElement(
        'h3', {}, "Hope you enjoy the journey with me.Don/'t stop believing:)"
    ),
    React.createElement(
        'ul', {}, [
        React.createElement(
            'li', {}, "1st"
        ),
        React.createElement(
            'li', {}, "2nd"
        ),
        React.createElement(
            'li', {}, "3rd"
        )
    ]
    )
]
)

ReactDOM.render(elementP70, dom);
