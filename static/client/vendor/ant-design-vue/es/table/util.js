import _toConsumableArray from 'babel-runtime/helpers/toConsumableArray';
import _extends from 'babel-runtime/helpers/extends';
export function flatArray() {
  var data = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : [];
  var childrenName = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 'children';

  var result = [];
  var loop = function loop(array) {
    array.forEach(function (item) {
      if (item[childrenName]) {
        var newItem = _extends({}, item);
        delete newItem[childrenName];
        result.push(newItem);
        if (item[childrenName].length > 0) {
          loop(item[childrenName]);
        }
      } else {
        result.push(item);
      }
    });
  };
  loop(data);
  return result;
}

export function treeMap(tree, mapper) {
  var childrenName = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : 'children';

  return tree.map(function (node, index) {
    var extra = {};
    if (node[childrenName]) {
      extra[childrenName] = treeMap(node[childrenName], mapper, childrenName);
    }
    return _extends({}, mapper(node, index), extra);
  });
}

export function flatFilter(tree, callback) {
  return tree.reduce(function (acc, node) {
    if (callback(node)) {
      acc.push(node);
    }
    if (node.children) {
      var children = flatFilter(node.children, callback);
      acc.push.apply(acc, _toConsumableArray(children));
    }
    return acc;
  }, []);
}

// export function normalizeColumns (elements) {
//   const columns = []
//   React.Children.forEach(elements, (element) => {
//     if (!React.isValidElement(element)) {
//       return
//     }
//     const column = {
//       ...element.props,
//     }
//     if (element.key) {
//       column.key = element.key
//     }
//     if (element.type && element.type.__ANT_TABLE_COLUMN_GROUP) {
//       column.children = normalizeColumns(column.children)
//     }
//     columns.push(column)
//   })
//   return columns
// }

export function generateValueMaps(items) {
  var maps = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};

  (items || []).forEach(function (_ref) {
    var value = _ref.value,
        children = _ref.children;

    maps[value.toString()] = value;
    generateValueMaps(children, maps);
  });
  return maps;
}