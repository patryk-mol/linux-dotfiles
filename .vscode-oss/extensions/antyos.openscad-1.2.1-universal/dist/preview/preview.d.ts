/**-----------------------------------------------------------------------------
 * Preview
 *
 * Stores a single instance of OpenSCAD
 *----------------------------------------------------------------------------*/
import * as vscode from 'vscode';
import { OpenscadExecutable } from './openscad-exe';
/** Open an instance of OpenSCAD to preview a file */
export declare class Preview {
    private readonly openscadExecutable;
    readonly uri: vscode.Uri;
    readonly hasGui: boolean;
    private readonly _process;
    private _isRunning;
    private _onKilledCallbacks;
    /** Launch an instance of OpenSCAD to prview a file */
    constructor(openscadExecutable: OpenscadExecutable, uri: vscode.Uri, hasGui: boolean, arguments_?: string[]);
    /** Kill child process */
    dispose(): void;
    /** Returns if the given Uri is equivalent to the preview's Uri */
    match(uri: vscode.Uri, hasGui?: boolean): boolean;
    get isRunning(): boolean;
    /** On killed handlers */
    get onKilled(): (() => void)[];
}
