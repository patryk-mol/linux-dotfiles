/**-----------------------------------------------------------------------------
 * Preview Store
 *
 * Class to manage a Set of previews
 *----------------------------------------------------------------------------*/
import * as vscode from 'vscode';
import { OpenscadExecutable } from './openscad-exe';
import { Preview } from './preview';
/** Container of several Preview */
export declare class PreviewStore {
    private static readonly areOpenScadPreviewsContextKey;
    private readonly _previews;
    private _maxPreviews;
    /** Dispose of the PreviewStore */
    dispose(): void;
    /** Defines behavior for `PreviewStore[]` */
    [Symbol.iterator](): Iterator<Preview>;
    /** Create a new PreviewStore with a max number of previews */
    constructor(maxPreviews?: number);
    /**
     * Find a resource in the PreviewStore by uri
     * @returns {Preview | undefined} Preview if found, otherwise undefined
     */
    get(resource: vscode.Uri, hasGui?: boolean): Preview | undefined;
    /** Add a preview to PreviewStore */
    add(preview: Preview): void;
    /** Create new preview (if not one with same uri) and then add it. */
    createAndAdd(openscadExecutable: OpenscadExecutable, uri: vscode.Uri, arguments_?: string[]): Preview | undefined;
    /** Delete and dispose of a preview. */
    delete(preview: Preview, informUser?: boolean): void;
    /** Functionally same as dispose() but without super.dispose(). */
    deleteAll(informUser?: boolean): void;
    /** Get the list of all open URIs. */
    getUris(): vscode.Uri[];
    /** Create progress bar for exporting. */
    makeExportProgressBar(preview: Preview): void;
    /** True if '-o' or '--o' (output) are not in the arguments list */
    static hasGui(arguments_?: string[]): boolean;
    /** Returns size (length) of PreviewStore. */
    get size(): number;
    get maxPreviews(): number;
    set maxPreviews(number_: number);
    /** Set vscode context 'areOpenPreviews'. Used in 'when' clauses. */
    private setAreOpenPreviews;
}
