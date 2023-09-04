/**-----------------------------------------------------------------------------
 * Preview Manager
 *
 * Class for adding / removing OpenSCAD previews to a previewStore
 *----------------------------------------------------------------------------*/
import * as vscode from 'vscode';
import { ExportFileExtension } from 'src/export/export-file-extensions';
/** Manager of multiple Preview objects */
export declare class PreviewManager {
    private previewStore;
    private config;
    private variableResolver;
    private openscadExecutableManager;
    /** Opens file in OpenSCAD */
    openFile(mainUri?: vscode.Uri, allUris?: vscode.Uri[], arguments_?: string[]): Promise<void>;
    /** Export file */
    exportFile(mainUri?: vscode.Uri, allUris?: vscode.Uri[], fileExtension?: ExportFileExtension | 'auto', useSaveDialogue?: boolean): Promise<void>;
    /** Prompt user for instances to kill */
    kill(autoKill?: boolean): Promise<void>;
    /** Kill all the current previews */
    killAll(): void;
    /** Constructor */
    constructor();
    /** Run when change configuration event */
    onDidChangeConfiguration(config: vscode.WorkspaceConfiguration): void;
    /** Gets the uri of the active editor */
    private getActiveEditorUri;
    /** Prompts user for export name and location */
    private promptForExport;
    /** Returns if the current URI with arguments (output Y/N) can be opened */
    private canOpenNewPreview;
}
