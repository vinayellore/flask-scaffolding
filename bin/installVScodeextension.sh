#!/bin/bash
echo -e "\nChecking if Visual studio code command is installed:"
if ! [ -x "$(command -v code)" ]; then
  echo -e '\nError: code command not found.'
  echo -e "\n1. In VS Code press CMD+SHIFT+P"
  echo -e "\n2. Search and select \"Install 'code' command in PATH\""
  echo -e "\nDo npm install again."
  exit 0
fi

echo -e "Installing recommended vscode extensions:"
echo -e "\nEditorConfig for VS Code"
code --install-extension EditorConfig.EditorConfig --force
echo -e "\nDebugger for chrome"
code --install-extension msjsdiag.debugger-for-chrome --force
echo -e "Docstring for python function"
code --install-extension njpwerner.autodocstring --force
echo -e "Python installation in vs code"
code --install-extension ms-python.python --force