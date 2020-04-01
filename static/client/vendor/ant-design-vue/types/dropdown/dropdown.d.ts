// Project: https://github.com/vueComponent/ant-design-vue
// Definitions by: akki-jat <https://github.com/akki-jat>
// Definitions: https://github.com/vueComponent/ant-design-vue/types

import { AntdComponent } from '../component';
import { Menu } from '../menu/menu';
import { DropdownButton } from './dropdown-button';

export declare class Dropdown extends AntdComponent {
  static Button: typeof DropdownButton;

  /**
   * the trigger mode which executes the drop-down action
   * @default ['hover']
   * @type string[]
   */
  trigger: Array<'click' | 'hover' | 'contextmenu'>;

  /**
   * the dropdown menu
   * @type () => Menu
   */
  overlay: any;

  /**
   * Class name of the dropdown root element
   * @type string
   */
  overlayClassName: string;

  /**
   * Style of the dropdown root element
   * @type object
   */
  overlayStyle: object;

  /**
   * whether the dropdown menu is visible
   * @type boolean
   */
  visible: boolean;

  /**
   * whether the dropdown menu is disabled
   * @type boolean
   */
  disabled: boolean;

  /**
   * to set the ontainer of the dropdown menu. The default is to create a div element in body, you can reset it to the scrolling area and make a relative reposition.
   * @default () => document.body
   * @type Function
   */
  getPopupContainer: (triggerNode?: any) => HTMLElement;

  /**
   * placement of pop menu: bottomLeft bottomCenter bottomRight topLeft topCenter topRight
   * @default 'bottomLeft'
   * @type string
   */
  placement: 'topLeft' | 'topCenter' | 'topRight' | 'bottomLeft' | 'bottomCenter' | 'bottomRight';
}
