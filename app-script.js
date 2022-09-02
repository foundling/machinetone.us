// backup of google app script that runs on mt google sheets db.
// does:
// - add 'date added' when a new artist is created.

// The column you want to check if something is entered.
const COLUMNTOCHECK = 1; // columns start at 1, not 0. 
// Where you want the date time stamp offset from the input location. [row, column]
const ROW_TO_START_CHECK = 2;
const DATETIMELOCATION = [0,1]; // offset down zero columns and to the right one column, where date added is stored.
// Sheet you are working on
const SHEETNAME = 'Artist'
 
function addDateOnCellCreation(ss, sheet) {
    if( sheet.getSheetName() == SHEETNAME ) {
      const selectedCell = ss.getActiveCell();
      //checks the column to ensure it is on the one we want to cause the date to appear.
      if( selectedCell.getColumn() == COLUMNTOCHECK && selectedCell.getRow() >= ROW_TO_START_CHECK && selectedCell.getValue().trim()) {
        const dateTimeCell = selectedCell.offset(DATETIMELOCATION[0],DATETIMELOCATION[1]);
        dateTimeCell.setValue(new Date());
      }
    }
  }
function onEdit(e) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getActiveSheet();
  //checks that we're on the correct sheet.
  addDateOnCellCreation(ss, sheet);
}
