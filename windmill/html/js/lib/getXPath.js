//Used for getting xpaths for elements in the DOM based on a given node
function getXPath(node, path) {
    path = path || [];

    if(node.parentNode) {
      path = getXPath(node.parentNode, path);
    }

    if(node.previousSibling) {
      var count = 1;
      var sibling = node.previousSibling
      do {
        if(sibling.nodeType == 1 && sibling.nodeName == node.nodeName) {count++;}
        sibling = sibling.previousSibling;
      } while(sibling);
      if(count == 1) {count = null;}
    } else if(node.nextSibling) {
      var sibling = node.nextSibling;
      do {
        if(sibling.nodeType == 1 && sibling.nodeName == node.nodeName) {
          var count = 1;
          sibling = null;
        } else {
          var count = null;
          sibling = sibling.previousSibling;
        }
      } while(sibling);
    }

    if(node.nodeType == 1) {
      path.push(node.nodeName.toLowerCase() + (node.id ? "[@id='"+node.id+"']" : count > 0 ? "["+count+"]" : ''));
    }
    return path;
  };
  
  function getXSPath(node){
    var xpArray = getXPath(node);
    console.log(xpArray);
    var index = null;
    //Find the last id'd node in the path and set that as the index
    for (var i = 0; i < xpArray.length; i++){
      if (xpArray[i].indexOf('[@') != -1 ){
        index = i;
        console.log(index);
      }
    }
    
    var stringXpath = '';
    
    //build the path from the index
    if ((index == null) || ($('absXpaths').checked)){
      stringXpath = xpArray.join('/');
      stringXpath = '/'+stringXpath;
      stringXpath = stringXpath.replace('//','/'); 
    }
    else {
      stringXpath = '//'+xpArray[index];
      index++;
      
      //build the rest of the string
      while (index < xpArray.length){
        stringXpath += '/' + xpArray[index];
        index++;
      }
    }
    
    // if ($('absXpaths').checked){
    //   stringXpath = stringXpath.replace(/\[@.*?\]/g, '');
    // }
    
  return stringXpath;
}