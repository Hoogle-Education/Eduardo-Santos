# Operadores logicos

Equacionando com a logica booleana.

## And

O `and` retorna `True` se ambos forem `True`.

Exemplo: agua e pó de café, consigo fazer um café:

|   `p`   |   `q`   | `p and q` |
| :-----: | :-----: | :-------: |
| `True`  | `True`  |  `True`   |
| `True`  | `False` |  `False`  |
| `False` | `True`  |  `False`  |
| `False` | `False` |  `False`  |

## Or

O `or` retorna `True` se pelo menos um for verdade.

Exemplo: agua ou suco, consigo matar a sede?

|   `p`   |   `q`   | `p or q` |
| :-----: | :-----: | :------: |
| `True`  | `True`  |  `True`  |
| `True`  | `False` |  `True`  |
| `False` | `True`  |  `True`  |
| `False` | `False` | `False`  |

## Precedencia de operadores

Uma operação que precede a outra.

Exemplo: multiplicação vs. soma
Exemplo: primeira condição do `or` e a segunda condição

### Uso avançado

```py
# o usuario so sera deletado se o primeiro membro do 'or' retornar True
# caso seja False, o segundo nem eh chamado
users.existesById(id) or users.deleteById(id)
```
